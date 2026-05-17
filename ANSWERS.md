# Teorifrågor

## Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
### Enhetstester testar en enskild del, kan vara en komponent eller enskild del av koden och skrivs oftast av utvecklarna själva och körs väldigt ofta, integrationstester testar hur enskilda delar samarbetar med varandra, ett exempel kan vara att man gör någonting på en websida och att det sen sparas ner i databasen.
### Regressionstester testar befintlig funktionalitet efter den har ändrats eller buggfixats och verifierar att något som fungerade innan en deploy tex inte slutat fungera. Detta kan köras i en CI/CD pipeline.
### Prestandatester testar systemets stabilitet, responstid och hur det klarar sig vid hög arbetsbelastning.
## Beskriv hur det går till när man arbetar med TDD.
### TDD är att man börjar med att skriva ett test som fallerar (eftersom koden inte finns ännu så kommer det fallera) för att sen skriva precis så mycket kod så att det slutar fallera. När det sen fungerar så refaktorerar (städar upp och snyggar till) man koden. Denna cykel upprepas för varje del av funktionalitet som skall byggas
## Beskriv hur BDD skiljer sig från TDD.
### BDD beskriver beteende ur användarens perspektiv gentemot TDD och dessa skrivs oftast tillsammans med kund och kan läsas av en som nödvändigtvis inte kan kod (kan skrivas med Gherkin). Man kan säga att TDD är utvecklarens perspektiv och BDD är användarens. BDD används med fördel för att undvika missförstånd av vad som ska byggas medan TDD fokuserar på hur koden är uppbyggd.
## Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. 
## Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
### Efter den här examinationsuppgiften så hade jag haft exakt detta upplägget som vi har gjort nu med enhet, integration och e2e tester. Detta för att man vill ha en hög testtäckning på både FE och BE. Jag kommer upptäcka buggar i ett tidigt skede med enhetstester och man testar så att de olika delarna av systemet fungerar ihop med integrationstesterna. Detta kommer spara mycket tid och pengar mot om det hade upptäckts i produktion eller innan release. Slutligen hade jag använt mig en e2e för att testa de viktigaste bitarna ur en riktig användares perspektiv

