def revisar_prompt(texto, tokens):
    if tokens > 100:
        print(f"⚠️ [EXCESO] '{texto}' es muy largo ({tokens} tokens)")
    else:
        print(f"✅ [OPTIMO] '{texto}' listo para enviar ({tokens} tokens)")
revisar_prompt("hola, como te ha ido en la vida", 102)
revisar_prompt("hola, como te ha ido en la vida", 98)
revisar_prompt("hola, como te ha ido en la vida", 10)
