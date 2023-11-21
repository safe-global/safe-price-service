kleros_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "challengePeriodDuration",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "governor",
        "outputs": [{"name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "arbitratorExtraData",
        "outputs": [{"name": "", "type": "bytes"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_beneficiary", "type": "address"},
            {"name": "_request", "type": "uint256"},
        ],
        "name": "amountWithdrawable",
        "outputs": [{"name": "total", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_sharedStakeMultiplier", "type": "uint256"}],
        "name": "changeSharedStakeMultiplier",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_beneficiary", "type": "address"},
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_cursor", "type": "uint256"},
            {"name": "_count", "type": "uint256"},
            {"name": "_roundCursor", "type": "uint256"},
            {"name": "_roundCount", "type": "uint256"},
        ],
        "name": "batchRequestWithdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "loserStakeMultiplier",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "countByStatus",
        "outputs": [
            {"name": "absent", "type": "uint256"},
            {"name": "registered", "type": "uint256"},
            {"name": "registrationRequest", "type": "uint256"},
            {"name": "clearingRequest", "type": "uint256"},
            {"name": "challengedRegistrationRequest", "type": "uint256"},
            {"name": "challengedClearingRequest", "type": "uint256"},
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_side", "type": "uint8"},
        ],
        "name": "fundAppeal",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "_tokenID", "type": "bytes32"}],
        "name": "getTokenInfo",
        "outputs": [
            {"name": "name", "type": "string"},
            {"name": "ticker", "type": "string"},
            {"name": "addr", "type": "address"},
            {"name": "symbolMultihash", "type": "string"},
            {"name": "status", "type": "uint8"},
            {"name": "numberOfRequests", "type": "uint256"},
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_disputeID", "type": "uint256"},
            {"name": "_ruling", "type": "uint256"},
        ],
        "name": "rule",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "challengerBaseDeposit",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_requesterBaseDeposit", "type": "uint256"}],
        "name": "changeRequesterBaseDeposit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_cursor", "type": "bytes32"},
            {"name": "_count", "type": "uint256"},
            {"name": "_filter", "type": "bool[8]"},
            {"name": "_oldestFirst", "type": "bool"},
            {"name": "_tokenAddr", "type": "address"},
        ],
        "name": "queryTokens",
        "outputs": [
            {"name": "values", "type": "bytes32[]"},
            {"name": "hasMore", "type": "bool"},
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "sharedStakeMultiplier",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "uint256"}],
        "name": "arbitratorDisputeIDToTokenID",
        "outputs": [{"name": "", "type": "bytes32"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "", "type": "uint256"}],
        "name": "tokensList",
        "outputs": [{"name": "", "type": "bytes32"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_request", "type": "uint256"},
            {"name": "_round", "type": "uint256"},
            {"name": "_contributor", "type": "address"},
        ],
        "name": "getContributions",
        "outputs": [{"name": "contributions", "type": "uint256[3]"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "arbitrator",
        "outputs": [{"name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "metaEvidenceUpdates",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "uint256"}],
        "name": "addressToSubmissions",
        "outputs": [{"name": "", "type": "bytes32"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_beneficiary", "type": "address"},
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_request", "type": "uint256"},
            {"name": "_cursor", "type": "uint256"},
            {"name": "_count", "type": "uint256"},
        ],
        "name": "batchRoundWithdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "winnerStakeMultiplier",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_evidence", "type": "string"},
        ],
        "name": "challengeRequest",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "requesterBaseDeposit",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "", "type": "bytes32"}],
        "name": "tokens",
        "outputs": [
            {"name": "name", "type": "string"},
            {"name": "ticker", "type": "string"},
            {"name": "addr", "type": "address"},
            {"name": "symbolMultihash", "type": "string"},
            {"name": "status", "type": "uint8"},
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_loserStakeMultiplier", "type": "uint256"}],
        "name": "changeLoserStakeMultiplier",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_request", "type": "uint256"},
            {"name": "_round", "type": "uint256"},
        ],
        "name": "getRoundInfo",
        "outputs": [
            {"name": "appealed", "type": "bool"},
            {"name": "paidFees", "type": "uint256[3]"},
            {"name": "hasPaid", "type": "bool[3]"},
            {"name": "feeRewards", "type": "uint256"},
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "tokenCount",
        "outputs": [{"name": "count", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_name", "type": "string"},
            {"name": "_ticker", "type": "string"},
            {"name": "_addr", "type": "address"},
            {"name": "_symbolMultihash", "type": "string"},
        ],
        "name": "requestStatusChange",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_beneficiary", "type": "address"},
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_request", "type": "uint256"},
            {"name": "_round", "type": "uint256"},
        ],
        "name": "withdrawFeesAndRewards",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_winnerStakeMultiplier", "type": "uint256"}],
        "name": "changeWinnerStakeMultiplier",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_arbitrator", "type": "address"},
            {"name": "_arbitratorExtraData", "type": "bytes"},
        ],
        "name": "changeArbitrator",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "_tokenID", "type": "bytes32"}],
        "name": "isPermitted",
        "outputs": [{"name": "allowed", "type": "bool"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_request", "type": "uint256"},
        ],
        "name": "getRequestInfo",
        "outputs": [
            {"name": "disputed", "type": "bool"},
            {"name": "disputeID", "type": "uint256"},
            {"name": "submissionTime", "type": "uint256"},
            {"name": "resolved", "type": "bool"},
            {"name": "parties", "type": "address[3]"},
            {"name": "numberOfRounds", "type": "uint256"},
            {"name": "ruling", "type": "uint8"},
            {"name": "arbitrator", "type": "address"},
            {"name": "arbitratorExtraData", "type": "bytes"},
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_challengePeriodDuration", "type": "uint256"}],
        "name": "changeTimeToChallenge",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MULTIPLIER_DIVISOR",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_registrationMetaEvidence", "type": "string"},
            {"name": "_clearingMetaEvidence", "type": "string"},
        ],
        "name": "changeMetaEvidence",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_challengerBaseDeposit", "type": "uint256"}],
        "name": "changeChallengerBaseDeposit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_governor", "type": "address"}],
        "name": "changeGovernor",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_tokenID", "type": "bytes32"}],
        "name": "executeRequest",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_tokenID", "type": "bytes32"},
            {"name": "_evidence", "type": "string"},
        ],
        "name": "submitEvidence",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"name": "_arbitrator", "type": "address"},
            {"name": "_arbitratorExtraData", "type": "bytes"},
            {"name": "_registrationMetaEvidence", "type": "string"},
            {"name": "_clearingMetaEvidence", "type": "string"},
            {"name": "_governor", "type": "address"},
            {"name": "_requesterBaseDeposit", "type": "uint256"},
            {"name": "_challengerBaseDeposit", "type": "uint256"},
            {"name": "_challengePeriodDuration", "type": "uint256"},
            {"name": "_sharedStakeMultiplier", "type": "uint256"},
            {"name": "_winnerStakeMultiplier", "type": "uint256"},
            {"name": "_loserStakeMultiplier", "type": "uint256"},
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "_name", "type": "string"},
            {"indexed": False, "name": "_ticker", "type": "string"},
            {"indexed": False, "name": "_symbolMultihash", "type": "string"},
            {"indexed": True, "name": "_address", "type": "address"},
        ],
        "name": "TokenSubmitted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "_tokenID", "type": "bytes32"},
            {"indexed": False, "name": "_registrationRequest", "type": "bool"},
        ],
        "name": "RequestSubmitted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "_requester", "type": "address"},
            {"indexed": True, "name": "_challenger", "type": "address"},
            {"indexed": True, "name": "_tokenID", "type": "bytes32"},
            {"indexed": False, "name": "_status", "type": "uint8"},
            {"indexed": False, "name": "_disputed", "type": "bool"},
            {"indexed": False, "name": "_appealed", "type": "bool"},
        ],
        "name": "TokenStatusChange",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "_tokenID", "type": "bytes32"},
            {"indexed": True, "name": "_contributor", "type": "address"},
            {"indexed": True, "name": "_request", "type": "uint256"},
            {"indexed": False, "name": "_round", "type": "uint256"},
            {"indexed": False, "name": "_value", "type": "uint256"},
        ],
        "name": "RewardWithdrawal",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "_metaEvidenceID", "type": "uint256"},
            {"indexed": False, "name": "_evidence", "type": "string"},
        ],
        "name": "MetaEvidence",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "_arbitrator", "type": "address"},
            {"indexed": True, "name": "_disputeID", "type": "uint256"},
            {"indexed": False, "name": "_metaEvidenceID", "type": "uint256"},
            {"indexed": False, "name": "_evidenceGroupID", "type": "uint256"},
        ],
        "name": "Dispute",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "_arbitrator", "type": "address"},
            {"indexed": True, "name": "_evidenceGroupID", "type": "uint256"},
            {"indexed": True, "name": "_party", "type": "address"},
            {"indexed": False, "name": "_evidence", "type": "string"},
        ],
        "name": "Evidence",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "_arbitrator", "type": "address"},
            {"indexed": True, "name": "_disputeID", "type": "uint256"},
            {"indexed": False, "name": "_ruling", "type": "uint256"},
        ],
        "name": "Ruling",
        "type": "event",
    },
]