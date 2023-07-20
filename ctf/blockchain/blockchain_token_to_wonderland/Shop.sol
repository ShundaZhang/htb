pragma solidity ^0.7.0;

import {SilverCoin} from "./SilverCoin.sol";

contract Shop {
    struct Item {
        string name;
        uint256 price;
        address owner;
    }

    Item[] public items;
    SilverCoin silverCoin;

    constructor(address _silverCoinAddress) {
        silverCoin = SilverCoin(_silverCoinAddress);
        items.push(Item("Diamond Necklace", 1_000_000, address(this)));
        items.push(Item("Ancient Stone", 70_000, address(this)));
        items.push(Item("Golden Key", 25_000_000, address(this)));
    }

    function buyItem(uint256 _index) public {
        Item memory _item = items[_index];
        require(_item.owner == address(this), "Item already sold");
        bool success = silverCoin.transferFrom(msg.sender, address(this), _item.price);
        require(success, "Payment failed!");
        items[_index].owner = msg.sender;
    }

    function viewItem(uint256 _index) public view returns (string memory, uint256, address) {
        return (items[_index].name, items[_index].price, items[_index].owner);
    }
}
