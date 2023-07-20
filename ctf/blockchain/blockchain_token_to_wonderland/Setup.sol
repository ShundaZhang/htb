// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import {SilverCoin} from "./SilverCoin.sol";
import {Shop} from "./Shop.sol";

contract Setup {
    Shop public immutable TARGET;

    constructor(address _player) payable {
        require(msg.value == 1 ether);
        SilverCoin silverCoin = new SilverCoin();
        silverCoin.transfer(_player, 100);
        TARGET = new Shop(address(silverCoin));
    }

    function isSolved(address _player) public view returns (bool) {
        (,, address ownerOfKey) = TARGET.viewItem(2);
        return ownerOfKey == _player;
    }
}
