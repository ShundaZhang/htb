// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

import "./Campaign2.sol";


contract Contract{
	address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0x7eb0803195b4686A8cADFdA14121E286Bde6a76A);

	CouncilWallet public creature = CouncilWallet(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	function attack2() public view returns (address[] memory){
		address[] memory councilMembers = new address[](11);
		for (uint256 i = 0; i < 11; i++) {
			councilMembers[i] = address(uint160(i));
		}

		return councilMembers;
	}

	function closeCampaign(bytes[] memory signatures, address to) public returns (address[] memory) {
		address[] memory voters = new address[](6);
		bytes32 data = keccak256(abi.encode(to));

		for (uint256 i = 0; i < signatures.length; i++) {
			// Get signer address
			address signer = data.toEthSignedMessageHash().recover(signatures[i]);

			// Ensure that signer is part of Council and has not already signed

			// Keep track of addresses that have already signed
			voters[i] = signer;
		}
		return voters;
	}

}

