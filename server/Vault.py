import os
import hvac

class Vault():
	def __init__(self, vault_url, vault_root_token):
		self.client = hvac.Client()
		self.client = hvac.Client(url=vault_url, token=vault_root_token)

	def getonetimetoken(self, token_lease_time, token_num_uses):
		token = self.client.create_token(policies=['root'], lease=token_lease_time, num_uses=token_num_uses)
		return token

