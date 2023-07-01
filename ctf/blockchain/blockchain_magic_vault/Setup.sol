// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Vault} from "./Vault.sol";

contract Setup {
    Vault public immutable TARGET;

    constructor() payable {
        require(msg.value == 1 ether);
        TARGET = new Vault();
    }

    function isSolved() public view returns (bool) {
        return TARGET.mapHolder() != address(TARGET);
    }
}
