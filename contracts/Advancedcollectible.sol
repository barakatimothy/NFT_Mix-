//An NFT contract 
//where it can be one of 3 dogs
//Randomly selected
// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";
contract advancedCollectible is ERC721{
    uint256 tokenCounter;
    bytes32 keyHash;
    uint256 fee;
    enum Breed{PUG, SHIBA_INU,ST_BERNARD}
    mapping(uint256 => Breed) public tokenIdToBreed;
    mapping (bytes32 => address) public requestIdTosender;
    event requestableCollectible(bytes32 indexed requestId,address requester)
    event breedAssigned(uint256 indexes tokenId,Breed breed)
constructor(address _VRFCoordinator,address _linkToken,bytes32 _keyHash,uint256 _fee)public
VRFConsumerBase(_VRFCoordinator,_linkToken)  
ERC721("Doggie","DOG")
{
tokenCounter =0;
keyHash = _keyHash;
fee =_fee; 
}
function createCollectible(strng memory tokenURI)public returns(bytes32){
    bytes32 requestId = requestRandomness(keyHash ,fee);
    requestIdTosender [requestId] = msg.sender;
    emit requestedCollectible(requestId,msg.sender   );
}
function fulfillRandomness(bytes32 requestId,uint256 randomNumber)internal override{
    Breed breed = breed(randomNumber % 3);
    uint256 newTokenId = tokenCounter;
    tokenIdToBreed[neTokenId] = breed;
    emit breedAssigned(newTokenId,breed  );
    address owner = requestIdTosender[requestId];
    _safeMint(owner , newTokenId);
    tokenCounter = tokenCounter +1;
    return newTokenId;
}
function setTokenURI(uint256 tokenId,string memory _tokenURI)public{
    //pug , shiba-inu ,st_benard
    require(_isApprovedOrOwner(_msgsender(),tokenId,"ERC721:caller is not owner or approved"));
    _setTokenURI (_tokenId, _tokenURI)
}
}