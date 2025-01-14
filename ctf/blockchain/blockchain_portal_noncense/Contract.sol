// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

//import "./Portal.sol";

contract Contract{

	mapping(string => address) public destinations;
	mapping(string => bool) public isPortalActive;
	bool isExpertStandby;

	function connect() public payable returns (bool) {
		destinations["orcKingdom"] = 0xFC31cde4aCbF2b1d2996a2C7f695E850918e4007;
		destinations["elfKingdom"] = 0x598136Fd1B89AeaA9D6825086B6E4cF9ad2BD4cF;
		destinations["dawrfKingdom"] = 0xFc2D16b59Ec482FaF3A8B1ee6E7E4E8D45Ec8bf1;
		isPortalActive["elfKingdom"] = true;
		isPortalActive["orcKingdom"] = true;
		isPortalActive["dawrfKingdom"] = true;

		isExpertStandby = true;

		return isExpertStandby;
	}

}

