dtss += unipi_uboot-overlay.dts
dtss += unipi_uboot_tpm-overlay.dts
dtss += antenna1-overlay.dts
dtss += lvc4-kms-v3d-pi4-overlay.dts

dtss += unipi_e410-overlay.dts
dtss += unipi_e411-overlay.dts
dtss += unipi_e412-overlay.dts
dtss += unipi_e413-overlay.dts
dtss += unipi_e414-overlay.dts
dtss += unipi_e415-overlay.dts
dtss += altboot-overlay.dts


dtbo-y = $(dtss:-overlay.dts=.dtbo)
targets  += $(dtbo-y)
always-y += $(dtbo-y)

%.dtbo: %-overlay.dts
	dtc -@ -O dtb -o $@ $<

overlays: $(targets)

.PHONY: overlays