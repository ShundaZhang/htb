// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./Portal.sol";

contract orcKingdom {
	
	address destinations0;
	address destinations1;
	address destinations2;
	bool isPortalActive;
	bool isExpertStandby;

	function connect() public payable returns (bool) {

		destinations0 = 0xFC31cde4aCbF2b1d2996a2C7f695E850918e4007;
		destinations1 = 0x598136Fd1B89AeaA9D6825086B6E4cF9ad2BD4cF;
		destinations2 = 0xFc2D16b59Ec482FaF3A8B1ee6E7E4E8D45Ec8bf1;
		isPortalActive = true;
		isExpertStandby = true;

		return isExpertStandby;
	}

}

contract Contract{
	PortalStation public creature;
	address public YOUR_CHALLENGE_CONTRACT_ADDRESS = address(0xACef632826fb9d4EF70cB70640b5F56b7474B3a9);
	orcKingdom public immutable new_addr;
	constructor() {
		creature = PortalStation(YOUR_CHALLENGE_CONTRACT_ADDRESS);
		new_addr = new orcKingdom();
	}

	

	function attack2() external view returns (address) {
		//creature.createPortal("orcKingdom");
		//creature.createPortal("elfKingdom");
		//creature.createPortal("dawrfKingdom");
		return address(new_addr);
	}

}

