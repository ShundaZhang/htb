// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./AuctionHouse.sol";


contract Contract{
        address payable public YOUR_CHALLENGE_CONTRACT_ADDRESS = payable(address(0xCc9226Ab913A9ede76CB3B828c97169121e78aEb));
	AuctionHouse public creature = AuctionHouse(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	receive() external payable {
	//function attack2(uint256 amount) payable external {
		//creature.transfer(value);
		YOUR_CHALLENGE_CONTRACT_ADDRESS.call{value: msg.value}("");
        }

}

