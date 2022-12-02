########################################################################################################################
# Variables
########################################################################################################################

ANSWER_PREFIX = answer_day_

PLAINTEXT_ANSWERS = ./answer_day_*.md
PLAINTEXT_KEY = theurdahesayopensesame

GPG_ARGUMENTS_ENCRYPT = --batch --yes -c --armor --passphrase "$(PLAINTEXT_KEY)"
GPG_ARGUMENTS_DECRYPT = --batch -d --passphrase "$(PLAINTEXT_KEY)"

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
encrypt: doEncrypt01 # Encrypt the answer files
encrypt: doEncrypt02

.PHONY: decrypt
decrypt: doDecrypt01 # Decrypt the answer files
decrypt: doDecrypt02

########################################################################################################################

doEncrypt01:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)01.md

doEncrypt02:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)02.md


########################################################################################################################

doDecrypt01:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)01.md.asc > ./$(ANSWER_PREFIX)01.md

doDecrypt02:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)02.md.asc > ./$(ANSWER_PREFIX)02.md
