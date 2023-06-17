proto:
	python3 -m grpc_tools.protoc -I. --python_out=../grpc_gen_code --pyi_out=../grpc_gen_code --grpc_python_out=../grpc_gen_code ./cctv_crud.proto
	python3 -m grpc_tools.protoc -I. --python_out=../grpc_gen_code --pyi_out=../grpc_gen_code --grpc_python_out=../grpc_gen_code ./business_logic.proto
	# sed -i 's/import cctv_crud_pb2/import grpc_gen_code.cctv_crud_pb2/g' ../grpc_gen_code/cctv_crud_pb2_grpc.py
	# sed -i 's/import business_logic_pb2/import grpc_gen_code.business_logic_pb2/g' ../grpc_gen_code/business_logic_pb2_grpc.py
