// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

import "./SilverCoin.sol";


contract Contract{
        address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0x8ee01E91eA96Ca640A68410b315700F1fB0cC534);
	address public source = address(0x1d90dafF0cBC880dfb579A985b17a17B47809414);
	SilverCoin public creature;
	constructor() {
		creature = new SilverCoin();
        }

	function attack2() external {
		creature.transfer(source, 25_000_000);
        }

	function balanceOf(address account) public view returns (uint256) {
        	return creature.balanceOf(account);
	}


}

