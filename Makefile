format_proto:
	@for pt in  $(shell find . | grep ".proto"); do \
		clang-format -i -style="{AlignConsecutiveAssignments: true,AlignConsecutiveDeclarations: true,AllowShortFunctionsOnASingleLine: None,BreakBeforeBraces: GNU,ColumnLimit: 0,IndentWidth: 4,Language: Proto}" $$pt ; \
	done
.PHONY: format_proto

grpc-gen:format_proto
	@for pt in  $(shell find . | grep ".proto"); do \
		python3 -m grpc_tools.protoc \
				-I . \
				--python_out=. \
				--grpc_python_out=. \
				$$pt ; \
	done
.PHONY: grpc-gen
