// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./AuctionHouse.sol";


contract Contract{
        address payable public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0x8ee01E91eA96Ca640A68410b315700F1fB0cC534);
	AuctionHouse public creature(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	function attack2(uint256 amount) external {
		//creature.transfer(value);
		YOUR_CHALLENGE_CONTRACT_ADDRESS.call{value: amount}("");
        }

}

