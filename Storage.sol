// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {

  // Define variables to store data
  string cert;
  string dpInfo;
  string emdLink;
  string paymentAdd;
  uint256 price;
  string sc;
  
 function store_data(string memory _cert, string memory _dpInfo, string memory _emdLink, string memory _paymentAdd, uint256 _price, string memory _sc) public {
    cert = _cert;
    dpInfo = _dpInfo;
    emdLink = _emdLink;
    paymentAdd = _paymentAdd;
    price = _price;
    sc = _sc;
  }

  // Function to set all data at once
  function setData(string memory _cert, string memory _dpInfo, string memory _emdLink, string memory _paymentAdd, uint256 _price, string memory _sc) public {
    cert = _cert;
    dpInfo = _dpInfo;
    emdLink = _emdLink;
    paymentAdd = _paymentAdd;
    price = _price;
    sc = _sc;
  }

  // Function to retrieve individual data
  function getCert() public view returns (string memory) {
    return cert;
  }

  // Function to retrieve individual data (similar functions can be added for other data)
  function getDpInfo() public view returns (string memory) {
    return dpInfo;
  }

  //function to retrieve EMD_Link
    function getEmdLink() public view returns (string memory) {
        return emdLink;
    }

    //function to retrieve Payment Address
    function getPaymentAdd() public view returns (string memory) {
        return paymentAdd;
    }

    //function to retrieve Price
    function getPrice() public view returns (uint256) {
        return price;
    }

    //function to retrieve SC
    function getSC() public view returns (string memory) {
        return sc;
    }

}
