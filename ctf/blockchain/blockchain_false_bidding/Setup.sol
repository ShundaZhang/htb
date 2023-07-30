// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import {AuctionHouse} from "./AuctionHouse.sol";

contract Setup {
    AuctionHouse public immutable TARGET;

    constructor() payable {
        require(msg.value == 1 ether);
        TARGET = new AuctionHouse{value: .5 ether}();
    }

    function isSolved(address player) public view returns (bool) {
        return TARGET.keyOwner() == player;
    }
}
