// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Vault {
    struct Map {
        address holder;
    }

    Map map;
    address public owner;
    bytes32 private passphrase;
    uint256 public nonce;
    bool public isUnlocked;

    constructor() {
        owner = msg.sender;
        passphrase = bytes32(keccak256(abi.encodePacked(uint256(blockhash(block.timestamp)))));
        map = Map(address(this));
    }

    function mapHolder() public view returns (address) {
        return map.holder;
    }

    function claimContent() public {
        require(isUnlocked);
        map.holder = msg.sender;
    }

    function unlock(bytes16 _password) public {
        uint128 _secretKey = uint128(bytes16(_magicPassword()) >> 64);
        uint128 _input = uint128(_password);
        require(_input != _secretKey, "Case 1 failed");
        require(uint64(_input) == _secretKey, "Case 2 failed");
        require(uint64(bytes8(_password)) == uint64(uint160(owner)), "Case 3 failed");
        isUnlocked = true;
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
