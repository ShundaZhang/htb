// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {PortalStation} from "./Portal.sol";

contract Setup {
    PortalStation public immutable TARGET;

    constructor() payable {
        TARGET = new PortalStation();
    }

    function isSolved() public view returns (bool) {
        return TARGET.isPortalActive("orcKingdom");
    }
}
