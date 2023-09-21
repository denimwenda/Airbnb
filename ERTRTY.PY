# Define the custom prompt function
function prompt {
    $Prompt = "PS [$env:USERNAME]$('>' * ($nestedPromptLevel + 1)) "
    return $Prompt
}