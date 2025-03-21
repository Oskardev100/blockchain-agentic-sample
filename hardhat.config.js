require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

module.exports = {
  solidity: "0.8.20",
  networks: {
    ganache: {
      url: "http://127.0.0.1:7545",  // Ganache RPC
      accounts: [process.env.GANACHE_PRIVATE_KEY]  // Updated variable name
    }
  }
};