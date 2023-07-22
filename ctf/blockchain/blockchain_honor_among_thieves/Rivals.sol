// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Rivals {
    event Voice(uint256 indexed severity);

    bytes32 private encryptedFlag;
    bytes32 private hashedFlag;
    address public solver;

    constructor(bytes32 _encrypted, bytes32 _hashed) {
        encryptedFlag = _encrypted;
        hashedFlag = _hashed;
    }

    function talk(bytes32 _key) external {
        bytes32 _flag = _key ^ encryptedFlag;
        if (keccak256(abi.encode(_flag)) == hashedFlag) {
            solver = msg.sender;
            emit Voice(5);
        } else {
            emit Voice(block.timestamp % 5);
        }
    }
}
