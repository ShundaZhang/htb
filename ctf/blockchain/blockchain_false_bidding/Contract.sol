// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./AuctionHouse.sol";


contract Contract{
        address payable public YOUR_CHALLENGE_CONTRACT_ADDRESS = payable(address(0xA735e8f54a61031b17A2a855cB14c7C1fd298f6D));
	AuctionHouse public creature = AuctionHouse(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	function attack2(uint256 amount) payable external {
		//creature.transfer(value);
		YOUR_CHALLENGE_CONTRACT_ADDRESS.call{value: amount}("");
        }

}

