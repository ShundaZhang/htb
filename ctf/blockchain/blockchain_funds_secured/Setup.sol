// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.18;

import {Crowdfunding} from "./Campaign.sol";
import {CouncilWallet} from "./Campaign.sol";

contract Setup {
    Crowdfunding public immutable TARGET;
    CouncilWallet public immutable WALLET;

    constructor() payable {
        // Generate the councilMember array
        // which contains the addresses of the council members that control the multi sig wallet.
        address[] memory councilMembers = new address[](11);
        for (uint256 i = 0; i < 11; i++) {
            councilMembers[i] = address(uint160(i));
        }

        WALLET = new CouncilWallet(councilMembers);
        TARGET = new Crowdfunding(address(WALLET));

        // Transfer enough funds to reach the campaing's goal.
        (bool success,) = address(TARGET).call{value: 1100 ether}("");
        require(success, "Transfer failed");
    }

    function isSolved() public view returns (bool) {
        return address(TARGET).balance == 0;
    }
}
