// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Lockers} from "./Lockers.sol";

contract Setup {
    Lockers public immutable TARGET;

    constructor(
        string[] memory _users,
        string[] memory _passwords,
        string[] memory _itemNames,
        string[] memory _itemOwners,
        uint8[] memory _itemRarities
    ) payable {
        require(msg.value > 2 ether);
        TARGET = new Lockers{value: 2 ether}(_users, _passwords, _itemNames, _itemOwners, _itemRarities);
    }

    function isSolved() public view returns (bool) {
        return address(TARGET).balance == 0;
    }
}
