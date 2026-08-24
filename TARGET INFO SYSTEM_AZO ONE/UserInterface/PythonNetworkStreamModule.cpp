// «»ÃÀ ⁄‰ 

PyObject* netOnClickPacket(PyObject* poSelf, PyObject* poArgs)
{
	int index;
	if (!PyTuple_GetInteger(poArgs, 0, &index))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.SendOnClickPacket(index);

	return Py_BuildNone();
}

// ÷⁄ «”›·Â«

//ENABLE TARGET INFO SYSTEM_AZO ONE
PyObject* netSendTargetInfoLoadPacket(PyObject* poSelf, PyObject* poArgs)
{
	int iVID;
	if (!PyTuple_GetInteger(poArgs, 0, &iVID))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendTargetInfoLoadPacket(iVID);

	return Py_BuildNone();
}
//ENABLE TARGET INFO SYSTEM_AZO ONE

// «»ÕÀ ⁄‰ 

		{ "SendOnClickPacket",					netOnClickPacket,						METH_VARARGS },


// ÷⁄ «”›·Â«

//ENABLE TARGET INFO SYSTEM_AZO ONE
		{ "SendTargetInfoLoadPacket",			netSendTargetInfoLoadPacket,			METH_VARARGS },
//ENABLE TARGET INFO SYSTEM_AZO ONE