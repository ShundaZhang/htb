// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;
pragma abicoder v2;

contract AuctionHouse {
    struct Key {
        address owner;
    }

    struct Bidder {
        address addr;
        uint64 bid;
    }

    Key private phoenixKey = Key(address(0));
    uint32 public timeout;
    Bidder[] public bidders;
    mapping(address => bool) private blacklisted;
    uint32 public constant YEAR = 31556926;

    constructor() payable {
        timeout = uint32(block.timestamp);
        _newBidder(msg.sender, 0.5 ether);
    }

    receive() external payable {
        if ((uint64(msg.value) >= 2 * topBidder().bid) && (msg.sender != topBidder().addr) && (!blacklisted[msg.sender])&& (_isPayable(msg.sender))) {
            _newBidder(msg.sender, uint64(msg.value));
            timeout += YEAR;
        }
    }

    function keyOwner() external view returns (address) {
        return phoenixKey.owner;
    }

    function keyTransfer(address _newOwner) external {
        require(msg.sender == phoenixKey.owner);
        phoenixKey.owner = _newOwner;
    }

    function topBidder() public view returns (Bidder memory) {
        return bidders[bidders.length - 1];
    }

    modifier topBidderOnly() {
        require(msg.sender == topBidder().addr);
        _;
    }

    function withdrawFromAuction() public topBidderOnly {
        Bidder memory withdrawer = topBidder();
        bidders.pop();

        (bool success,) = payable(withdrawer.addr).call{value: withdrawer.bid / 2}("");
        if (success) {
            blacklisted[withdrawer.addr] = true;
            blacklisted[tx.origin] = true;
        }
    }

    function claimPrize() public topBidderOnly {
        require(uint32(block.timestamp) > timeout, "Still locked");
        require(phoenixKey.owner == address(0));
        phoenixKey.owner = topBidder().addr;
    }

    function _newBidder(address _address, uint64 _bid) private {
        bidders.push(Bidder(_address, _bid));
    }

    function _isPayable(address _address) private returns (bool) {
        (bool success,) = payable(_address).call{value: 0}("");
        return success;
    }
}
