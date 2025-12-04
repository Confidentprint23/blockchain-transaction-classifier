# fix_bft_data.py
import pickle

# Create mock BFT data
bft_data = {
    'bft_metrics': {
        'total_nodes': 1000,
        'byzantine_nodes': 150,
        'honest_nodes': 850,
        'byzantine_ratio': 0.15,
        'max_tolerable_bft': 333,
        'max_tolerable_practical': 250,
        'bft_safety_margin': 183,
        'is_bft_secure': True
    },
    'consensus_results': {
        'successful_consensus': 950,
        'failed_consensus': 50,
        'byzantine_attacks_blocked': 145
    },
    'bft_analyzer': None
}

# Save fixed file
with open('data/bft_data.pkl', 'wb') as f:
    pickle.dump(bft_data, f)

print("✅ Fixed bft_data.pkl created!")