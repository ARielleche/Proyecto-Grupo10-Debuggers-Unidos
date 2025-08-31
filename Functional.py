# Functional.py
import yaml
from pathlib import Path
from typing import List, Dict, Callable

PROBLEMS_PATH = Path(__file__).parent / "problems.yaml"

# Funciones puras (sin efectos secundarios)
def crear_pregunta(titulo: str, enunciado: str, pistas: List[str], etiquetas: List[str]) -> Dict:
    """Crea un diccionario representando una pregunta (función pura)"""
    return {
        "title": titulo,
        "prompt": enunciado,
        "hints": pistas,
        "tags": etiquetas
    }

def transformar_preguntas(preguntas: List[Dict], funcion_transformacion: Callable) -> List[Dict]:
    """Aplica una función de transformación a todas las preguntas (higher-order function)"""
    return list(map(funcion_transformacion, preguntas))

# Funciones con efectos secundarios (manejo de archivos)
def cargar_preguntas_existentes() -> List[Dict]:
    """Carga las preguntas existentes del archivo YAML"""
    if PROBLEMS_PATH.exists():
        with PROBLEMS_PATH.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or []
    return []

def guardar_preguntas(preguntas: List[Dict]):
    """Guarda las preguntas en el archivo YAML"""
    with PROBLEMS_PATH.open("w", encoding="utf-8") as f:
        yaml.dump(preguntas, f, allow_unicode=True, sort_keys=False)

# Composición de funciones
def agregar_preguntas(nuevas_preguntas: List[Dict]):
    """Agrega nuevas preguntas al archivo existente (composición de funciones)"""
    preguntas_existentes = cargar_preguntas_existentes()
    todas_las_preguntas = preguntas_existentes + nuevas_preguntas
    guardar_preguntas(todas_las_preguntas)

# Generador de preguntas (lazy evaluation)
def generar_preguntas_ejemplo():
    """Genera preguntas de ejemplo usando programación funcional"""
    
    # Datos de ejemplo (10 preguntas)
    datos_preguntas = [
        ("Suma dos números", "Escribe `suma(a, b)` que devuelva a + b", 
         ["Usa operadores aritméticos", "Devuelve el resultado"], 
         ["funciones", "aritmética"]),
         
        ("Factorial recursivo", "Implementa `factorial(n)` de forma recursiva",
         ["Caso base: factorial(0) = 1", "Caso recursivo: n * factorial(n-1)"],
         ["recursión", "matemáticas"]),
         
        ("Palíndromo", "Verifica si una palabra es palíndromo",
         ["Compara primero con último carácter", "Puedes usar slicing [::-1]"],
         ["strings", "algoritmos"]),
         
        ("Contar vocales", "Cuenta las vocales en un string",
         ["Itera sobre cada carácter", "Usa una lista de vocales"],
         ["strings", "bucles"]),
         
        ("Ordenar lista", "Implementa un algoritmo de ordenamiento",
         ["Puedes usar bubble sort", "O investigar otros algoritmos"],
         ["algoritmos", "ordenamiento"]),
         
        ("Fibonacci", "Genera la secuencia de Fibonacci",
         ["Usa recursión o iteración", "Fibonacci(0)=0, Fibonacci(1)=1"],
         ["matemáticas", "secuencias"]),
         
        ("Máximo común divisor", "Calcula el MCD de dos números",
         ["Usa el algoritmo de Euclides", "MCD(a, 0) = a"],
         ["matemáticas", "algoritmos"]),
         
        ("Invertir lista", "Invierte el orden de una lista",
         ["Puedes usar slicing", "O un bucle for inverso"],
         ["listas", "algoritmos"]),
         
        ("Contar palabras", "Cuenta palabras en un texto",
         ["Usa split() para dividir el texto", "Cuenta los elementos resultantes"],
         ["strings", "procesamiento de texto"]),
         
        ("Filter pares", "Filtra números pares de una lista",
         ["Usa filter con lambda", "O comprensión de listas"],
         ["funciones", "filter", "lambda"])
    ]
    
    # Usar map para transformar tuplas en diccionarios de preguntas
    return list(map(lambda x: crear_pregunta(*x), datos_preguntas))

# Función principal para el bot
def cargar_preguntas_funcional():
    """Función que será llamada desde bot.py para cargar preguntas usando paradigma funcional"""
    print("Cargando preguntas con enfoque funcional...")
    
    try:
        nuevas_preguntas = generar_preguntas_ejemplo()
        agregar_preguntas(nuevas_preguntas)
        print(f"✅ Se agregaron {len(nuevas_preguntas)} preguntas funcionales")
        return True
    except Exception as e:
        print(f"❌ Error en enfoque funcional: {e}")
        return False

# Tests funcionales (pueden ejecutarse independientemente)
if __name__ == "__main__":
    # Ejemplo de uso
    print("Testing Functional.py...")
    
    # Probar la creación de preguntas
    pregunta_ejemplo = crear_pregunta(
        "Test", "Función de prueba", ["pista1", "pista2"], ["test"]
    )
    print("Pregunta creada:", pregunta_ejemplo)
    
    # Probar la carga y guardado
    cargar_preguntas_funcional()
    print("Preguntas cargadas exitosamente!")