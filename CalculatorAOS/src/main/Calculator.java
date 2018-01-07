package main;

import java.util.List;

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;
import javax.xml.ws.Holder;

import com.oracle.xmlns.internal.webservices.jaxws_databinding.WebParamMode;

@WebService
public class Calculator {

	@WebMethod
	public int add(int op1, int op2) {
		return op1 + op2;
	}

	@WebMethod
	public int substract(int op1, int op2) {
		return op1 - op2;
	}

	@WebMethod
	public int multiply(int op1, int op2) {
		return op1 * op2;
	}

	@WebMethod
	public int divide(int op1, int op2) {
		return op1 / op2;
	}

	public void addMultiply(int op1, int op2, @WebParam(mode = WebParam.Mode.OUT) Holder<Integer> add,
			@WebParam(mode = WebParam.Mode.OUT) Holder<Integer> multiply) {
		add.value = new Integer(op1 + op2);
		multiply.value = new Integer(op1 * op2);
	}

	public void addIntVector(int[] operandsVector, @WebParam(mode = WebParam.Mode.OUT) Holder<Integer> add) {
		add.value = 0;
		for (int operand : operandsVector) {
			add.value += operand;
		}
	}

	public void addIntList(List<Integer> operandsList, @WebParam(mode = WebParam.Mode.OUT) Holder<Integer> add) {
		add.value = 0;
		for (Integer operand : operandsList) {
			add.value += operand;			
		}
	}

}
