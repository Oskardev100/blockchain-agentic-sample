const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log(`Deploying contract with the account: ${deployer.address}`);

  const Escrow = await hre.ethers.getContractFactory("Escrow");
  const escrow = await Escrow.deploy(deployer.address, hre.ethers.parseEther("1"));

  await escrow.waitForDeployment();
  console.log(`Escrow contract deployed at: ${await escrow.getAddress()}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
