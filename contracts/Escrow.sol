// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Escrow {
    address payable public buyer;
    address payable public seller;
    uint256 public price;
    bool public isPaid;

    constructor(address payable _seller, uint256 _price) {
        buyer = payable(msg.sender);
        seller = _seller;
        price = _price;
        isPaid = false;
    }

    function deposit() external payable {
        require(msg.value == price, "Incorrect amount sent");
        isPaid = true;
    }

    function releaseFunds() external {
        require(isPaid, "Payment not made");
        seller.transfer(price);
    }
}
