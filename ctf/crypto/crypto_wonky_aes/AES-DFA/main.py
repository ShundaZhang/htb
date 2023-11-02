from DFA_Attack import *

cipher_text = [
	b'58ea4b0e60992e90feae9bce0e2c4c85',
	b'0433b85f47b96561fd31dc34ba42d026',
	b'6cdf3188773690f76d2da311fabeba23',
	b'31b748ff3cc394adde9df073e4f5b185',
	b'4885803db07aa1e02d1c0c5162a1cacf',
	b'0be82ee9c00ab64309b1f8e11e286cdc',
	b'083573db3033eff36b990280aa4ea925',
	b'3754b949b25b6fa20c036867bcaad8a7'
]

faulted_texts = [
	b'ffea4b0e60992e08feae75ce0e5f4c85',
	b'8f33b85f47b96571fd314334babad026',
	b'6c4f3188ec3690f76d2da30efabe2323',
	b'319848ffaec394adde9df045e4f5a985',
	b'4885de3db0d5a1e0ae1c0c5162a1cafb',
	b'0be837e9c02bb643c5b1f8e11e286c9b',
	b'0835739d3033f1f36b180280984ea925',
	b'3754b989b25b90a20c3a6867b8aad8a7'
]


key = DFA_attack(
		cipher=cipher_text,
		faults=faulted_texts,
		rounds=11
	).Crack_key()

print(key)

# https://blog.quarkslab.com/differential-fault-analysis-on-white-box-aes-implementations.html
