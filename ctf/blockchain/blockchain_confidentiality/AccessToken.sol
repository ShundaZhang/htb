// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.19;

import {ERC721} from "./lib/ERC721.sol";
import {Owned} from "./lib/Owned.sol";

contract AccessToken is ERC721, Owned {
    uint256 public currentSupply;
    bytes[] public usedSignatures;

    bytes32 public constant approvalHash = 0x4ed1c9f7e3813196653ad7c62857a519087860f86aff4bc7766c8af8756a72ba;

    constructor(address _owner) Owned(_owner) ERC721("AccessToken", "ACT") {}

    function safeMint(address to) public onlyOwner returns (uint256) {
        return _safeMintInternal(to);
    }

    function safeMintWithSignature(bytes memory signature, address to) external returns (uint256) {
        require(_verifySignature(signature), "Not approved");
        require(!_isSignatureUsed(signature), "Signature already used");

        usedSignatures.push(signature);

        return _safeMintInternal(to);
    }

    function _verifySignature(bytes memory signature) internal view returns (bool) {
        (uint8 v, bytes32 r, bytes32 s) = deconstructSignature(signature);
        address signer = ecrecover(approvalHash, v, r, s);

        return signer == owner;
    }

    function _isSignatureUsed(bytes memory _signature) internal view returns (bool) {
        for (uint256 i = 0; i < usedSignatures.length; i++) {
            if (keccak256(_signature) == keccak256(usedSignatures[i])) {
                return true;
            }
        }
        return false;
    }

    function _safeMintInternal(address to) internal returns (uint256) {
        currentSupply += 1;
        _safeMint(to, currentSupply);
        return currentSupply;
    }

    // ##### Signature helper utilities

    // utility function to deconstruct a signature returning (v, r, s)
    function deconstructSignature(bytes memory signature) public pure returns (uint8, bytes32, bytes32) {
        bytes32 r;
        bytes32 s;
        uint8 v;
        // ecrecover takes the signature parameters, and the only way to get them
        // currently is to use assembly.
        /// @solidity memory-safe-assembly
        assembly {
            r := mload(add(signature, 0x20))
            s := mload(add(signature, 0x40))
            v := byte(0, mload(add(signature, 0x60)))
        }
        return (v, r, s);
    }

    function constructSignature(uint8 v, bytes32 r, bytes32 s) public pure returns (bytes memory) {
        return abi.encodePacked(r, s, v);
    }
}
