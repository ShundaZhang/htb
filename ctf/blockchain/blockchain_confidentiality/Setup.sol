// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.19;

import {AccessToken} from "./AccessToken.sol";

contract Setup {
    AccessToken public immutable TARGET;

    constructor(address _owner, bytes memory signature) {
        TARGET = new AccessToken(_owner);

        // Secure 1 AccessToken for myself
        TARGET.safeMintWithSignature(signature, address(this));
    }

    function isSolved(address _player) public view returns (bool) {
        return TARGET.balanceOf(_player) > 0;
    }
}
