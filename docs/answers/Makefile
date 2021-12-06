########################################################################################################################
# Variables
########################################################################################################################

ANSWER_PREFIX = answer_day_

PLAINTEXT_ANSWERS = ./answer_day_*.md
PLAINTEXT_KEY = theurdahesayopensesame

GPG_ARGUMENTS_ENCRYPT = -c --armor --passphrase "$(PLAINTEXT_KEY)"
GPG_ARGUMENTS_DECRYPT = -d --passphrase "$(PLAINTEXT_KEY)"

########################################################################################################################
# `make help` Needs to be first so it is ran when just `make` is called
########################################################################################################################

.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' ${MAKEFILE_LIST} |\
	sort -k1,1 |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[1m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: # Clean plaintext answers
	rm -rf $(PLAINTEXT_ANSWERS) && \
	:

########################################################################################################################

.PHONY: encrypt
encrypt: doEncrypt01 doEncrypt02 doEncrypt03 doEncrypt04 # Encrypt the answer files

.PHONY: decrypt
decrypt: doDecrypt01 doDecrypt02 doDecrypt03 doDecrypt04 # Decrypt the answer files

########################################################################################################################

doEncrypt01:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)01.md

doEncrypt02:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)02.md

doEncrypt03:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)03.md

doEncrypt04:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)04.md

########################################################################################################################

doDecrypt01:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)01.md.asc > ./$(ANSWER_PREFIX)01.md

doDecrypt02:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)02.md.asc > ./$(ANSWER_PREFIX)02.md

doDecrypt03:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)03.md.asc > ./$(ANSWER_PREFIX)03.md

doDecrypt04:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)04.md.asc > ./$(ANSWER_PREFIX)04.md

