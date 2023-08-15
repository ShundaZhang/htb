// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract PortalStation {
    
    mapping(string => address) public destinations;
    mapping(string => bool) public isPortalActive;
    bool isExpertStandby;

    constructor() {
        destinations["orcKingdom"] = 0xFC31cde4aCbF2b1d2996a2C7f695E850918e4007;
        destinations["elfKingdom"] = 0x598136Fd1B89AeaA9D6825086B6E4cF9ad2BD4cF;
        destinations["dawrfKingdom"] = 0xFc2D16b59Ec482FaF3A8B1ee6E7E4E8D45Ec8bf1;
        isPortalActive["elfKingdom"] = true;
    }

    function requestPortal(string calldata _destination) public payable {
        require(destinations[_destination] != address(0));
        require(isExpertStandby, "Portal expert has a day off");
        //require(msg.value > 1337 ether);

        isPortalActive[_destination] = true;
    }

    function createPortal(string calldata _destination) public {
        require(destinations[_destination] != address(0));
        
        (bool success, bytes memory retValue) = destinations[_destination].delegatecall(abi.encodeWithSignature("connect()"));
        require(success, "Portal destination is currently not available");
        require(abi.decode(retValue, (bool)), "Connection failed");
    }

}
