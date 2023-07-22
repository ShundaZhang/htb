// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Rivals} from "./Rivals.sol";

contract Setup {
    Rivals public immutable TARGET;

    constructor(bytes32 _encryptedFlag, bytes32 _hashed) payable {
        TARGET = new Rivals(_encryptedFlag, _hashed);
    }

    function isSolved(address _player) public view returns (bool) {
        return TARGET.solver() == _player;
    }
}
