// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.18;

import {ECDSA} from "./lib/ECDSA.sol";

/// @notice MultiSignature wallet used to end the Crowdfunding and transfer the funds to a desired address
contract CouncilWallet {
    using ECDSA for bytes32;

    address[] public councilMembers;

    /// @notice Register the 11 council members in the wallet
    constructor(address[] memory members) {
        require(members.length == 11);
        councilMembers = members;
    }

    /// @notice Function to close crowdfunding campaign. If at least 6 council members have signed, it ends the campaign and transfers the funds to `to` address
    function closeCampaign(bytes[] memory signatures, address to, address payable crowdfundingContract) public {
        address[] memory voters = new address[](6);
        bytes32 data = keccak256(abi.encode(to));

        for (uint256 i = 0; i < signatures.length; i++) {
            // Get signer address
            address signer = data.toEthSignedMessageHash().recover(signatures[i]);

            // Ensure that signer is part of Council and has not already signed
            require(signer != address(0), "Invalid signature");
            require(_contains(councilMembers, signer), "Not council member");
            require(!_contains(voters, signer), "Duplicate signature");

            // Keep track of addresses that have already signed
            voters[i] = signer;
            // 6 signatures are enough to proceed with `closeCampaign` execution
            if (i > 5) {
                break;
            }
        }

        Crowdfunding(crowdfundingContract).closeCampaign(to);
    }

    /// @notice Returns `true` if the `_address` exists in the address array `_array`, `false` otherwise
    function _contains(address[] memory _array, address _address) private pure returns (bool) {
        for (uint256 i = 0; i < _array.length; i++) {
            if (_array[i] == _address) {
                return true;
            }
        }
        return false;
    }
}

contract Crowdfunding {
    address owner;

    uint256 public constant TARGET_FUNDS = 1000 ether;

    constructor(address _multisigWallet) {
        owner = _multisigWallet;
    }

    receive() external payable {}

    function donate() external payable {}

    /// @notice Delete contract and transfer funds to specified address. Can only be called by owner
    function closeCampaign(address to) public {
        require(msg.sender == owner, "Only owner");
        selfdestruct(payable(to));
    }
}
