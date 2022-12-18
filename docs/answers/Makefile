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
encrypt: doEncrypt03
encrypt: doEncrypt04
encrypt: doEncrypt05
encrypt: doEncrypt06
encrypt: doEncrypt07
encrypt: doEncrypt08
encrypt: doEncrypt09
encrypt: doEncrypt10
encrypt: doEncrypt11
encrypt: doEncrypt12
encrypt: doEncrypt13
encrypt: doEncrypt14
encrypt: doEncrypt15
encrypt: doEncrypt16
encrypt: doEncrypt17

.PHONY: decrypt
decrypt: doDecrypt01 # Decrypt the answer files
decrypt: doDecrypt02
decrypt: doDecrypt03
decrypt: doDecrypt04
decrypt: doDecrypt05
decrypt: doDecrypt06
decrypt: doDecrypt07
decrypt: doDecrypt08
decrypt: doDecrypt09
decrypt: doDecrypt10
decrypt: doDecrypt11
decrypt: doDecrypt12
decrypt: doDecrypt13
decrypt: doDecrypt14
decrypt: doDecrypt15
decrypt: doDecrypt16
decrypt: doDecrypt17

########################################################################################################################

doEncrypt01:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)01.md

doEncrypt02:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)02.md

doEncrypt03:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)03.md

doEncrypt04:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)04.md

doEncrypt05:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)05.md

doEncrypt06:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)06.md

doEncrypt07:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)07.md

doEncrypt08:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)08.md

doEncrypt09:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)09.md

doEncrypt10:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)10.md

doEncrypt11:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)11.md

doEncrypt12:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)12.md

doEncrypt13:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)13.md

doEncrypt14:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)14.md

doEncrypt15:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)15.md

doEncrypt16:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)16.md

doEncrypt17:
	gpg $(GPG_ARGUMENTS_ENCRYPT) ./$(ANSWER_PREFIX)17.md

########################################################################################################################

doDecrypt01:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)01.md.asc > ./$(ANSWER_PREFIX)01.md

doDecrypt02:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)02.md.asc > ./$(ANSWER_PREFIX)02.md

doDecrypt03:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)03.md.asc > ./$(ANSWER_PREFIX)03.md

doDecrypt04:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)04.md.asc > ./$(ANSWER_PREFIX)04.md

doDecrypt05:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)05.md.asc > ./$(ANSWER_PREFIX)05.md

doDecrypt06:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)06.md.asc > ./$(ANSWER_PREFIX)06.md

doDecrypt07:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)07.md.asc > ./$(ANSWER_PREFIX)07.md

doDecrypt08:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)08.md.asc > ./$(ANSWER_PREFIX)08.md

doDecrypt09:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)09.md.asc > ./$(ANSWER_PREFIX)09.md

doDecrypt10:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)10.md.asc > ./$(ANSWER_PREFIX)10.md

doDecrypt11:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)11.md.asc > ./$(ANSWER_PREFIX)11.md

doDecrypt12:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)12.md.asc > ./$(ANSWER_PREFIX)12.md

doDecrypt13:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)13.md.asc > ./$(ANSWER_PREFIX)13.md

doDecrypt14:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)14.md.asc > ./$(ANSWER_PREFIX)14.md

doDecrypt15:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)15.md.asc > ./$(ANSWER_PREFIX)15.md

doDecrypt16:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)16.md.asc > ./$(ANSWER_PREFIX)16.md

doDecrypt17:
	gpg $(GPG_ARGUMENTS_DECRYPT) ./$(ANSWER_PREFIX)17.md.asc > ./$(ANSWER_PREFIX)17.md
