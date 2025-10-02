# lmstudio_utils.py

# Global conversation history
conversation = []

def interact_with_llm(prompt,
                      model,
                      temperature=0.7,
                      max_tokens=512,
                      top_p=1.0):
    """
    Interactúa con un modelo cargado en LM Studio mostrando todo el historial.
    """
    global conversation

    # Añadir el nuevo mensaje al historial
    conversation.append({"role": "user", "content": prompt})

    # Llamar al modelo
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p
    )

    # Extraer respuesta
    answer = response.choices[0].message.content.strip()

    # Añadir respuesta al historial
    conversation.append({"role": "assistant", "content": answer})

    # Mostrar todo el historial
    print("\n===== Conversación completa =====")
    for i, msg in enumerate(conversation, start=1):
        role = "👤 Usuario" if msg["role"] == "user" else "🤖 Asistente"
        print(f"{i}. {role}: {msg['content']}")
    print("=================================\n")

    return answer
