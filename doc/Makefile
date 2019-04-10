BUILD = ${REPO_HOME}/build/doc

define map_tex
  $(addprefix ${BUILD}/image/, $(notdir $(patsubst %.tex, %.pdf, ${1})))
endef

define rule_tex
$(call map_tex, ${1}) : ${1} 
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" pdflatex  -output-directory $(dir ${@}) $(basename ${<})
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" pdflatex  -output-directory $(dir ${@}) $(basename ${<})
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" pdflatex  -output-directory $(dir ${@}) $(basename ${<})
endef

IMAGE_SOURCES_TEX = $(wildcard ./image/*.tex)
IMAGE_TARGETS_TEX = $(foreach FILE, ${IMAGE_SOURCES_TEX}, $(call map_tex, ${FILE}))

$(foreach FILE,${IMAGE_SOURCES_TEX},$(eval $(call rule_tex,${FILE})))

${BUILD}/doc.pdf : ./doc.tex $(wildcard ./tex/* ./image/*)
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" pdflatex  -output-directory $(dir ${@}) $(basename ${<})
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" biber    --output_directory $(dir ${@}) $(basename ${<})
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" pdflatex  -output-directory $(dir ${@}) $(basename ${<})
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" biber    --output_directory $(dir ${@}) $(basename ${<})
	@TEXINPUTS="${TEXINPUTS}:.:${BUILD}" pdflatex  -output-directory $(dir ${@}) $(basename ${<})

.PHONY: image

dir   :
	@mkdir --parents ${BUILD}
	@mkdir --parents ${BUILD}/image

image :

all   : dir image ${BUILD}/doc.pdf

clean :
	@rm -rf ${BUILD}
