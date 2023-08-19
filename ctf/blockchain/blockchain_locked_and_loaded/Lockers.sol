// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Lockers {
    enum Rarity {
        Common,
        Rare,
        Epic,
        Mythic
    }

    struct Item {
        string name;
        string owner;
        Rarity rarity;
    }

    mapping(string => string) private users;
    mapping(string => address) private usernameToWallet;
    mapping(Rarity => uint256) public price;
    Item[] private items;

    constructor(
        string[] memory _users,
        string[] memory _passwords,
        string[] memory _itemNames,
        string[] memory _itemOwners,
        uint8[] memory _itemRarities
    ) payable {
        require(_users.length == _passwords.length);
        require((_itemNames.length == _itemOwners.length) && (_itemOwners.length == _itemRarities.length));

        for (uint256 i; i < _users.length;) {
            users[_users[i]] = _passwords[i];
            unchecked {
                ++i;
            }
        }

        for (uint256 i; i < _itemNames.length;) {
            items.push(Item(_itemNames[i], _itemOwners[i], Rarity(_itemRarities[i])));
            unchecked {
                ++i;
            }
        }

        price[Rarity.Common] = 1;
        price[Rarity.Rare] = 10;
        price[Rarity.Epic] = 100;
        price[Rarity.Mythic] = 1000000000000000000;
    }

    function putItem(string calldata name, string calldata owner, uint8 rarity) external {
        require(rarity < 3);
        items.push(Item(name, owner, Rarity(rarity)));
    }

    function viewItems(string calldata _name) external view returns (string memory, Rarity) {
        for (uint256 i = 0; i < items.length; ++i) {
            if (_strEquals(_name, items[i].name)) {
                return (items[i].owner, items[i].rarity);
            }
        }
        revert("NoSuchItem");
    }

    function retrieveItem(string calldata name, string calldata password) external {
        for (uint256 i = 0; i < items.length; ++i) {
            if (_strEquals(name, items[i].name)) {
                require(_strEquals(password, users[items[i].owner]), "Authentication Failed");
                delete items[i];
                break;
            }
        }
    }

    function transferItem(string calldata name, string calldata to, string calldata password) external {
        for (uint256 i = 0; i < items.length; ++i) {
            if (_strEquals(name, items[i].name)) {
                require(_strEquals(password, users[items[i].owner]), "Authentication Failed");
                items[i].owner = to;
                break;
            }
        }
    }

    function sellItem(string calldata name, string calldata password) external {
        uint256 index;
        Item memory _item;
        string memory prevOwner;

        for (uint256 i = 0; i < items.length; ++i) {
            if (_strEquals(name, items[i].name)) {
                require(_strEquals(password, users[items[i].owner]), "Authentication Failed");
                _item = items[i];
                prevOwner = items[i].owner;
                index = i;
            }
        }

        require(bytes(_item.name).length > 0, "Item does not exist");

        _item.owner = "Vendor";

        (bool success,) = usernameToWallet[prevOwner].call{value: price[_item.rarity]}("");
        require(success);
        delete items[index];
    }

    function getLocker(string calldata username, string calldata password) external {
        require(bytes(users[username]).length == 0, "User already exists");
        require(!_strEquals(username, "Vendor"), "Only the true vendor can use this name!");
        users[username] = password;
        usernameToWallet[username] = msg.sender;
    }

    function _strEquals(string calldata _first, string memory _second) private pure returns (bool) {
        return keccak256(abi.encode(_first)) == keccak256(abi.encode(_second));
    }
}
